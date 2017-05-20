// Code generated by protoc-gen-go. DO NOT EDIT.
// source: can.proto

/*
Package can is a generated protocol buffer package.

It is generated from these files:
	can.proto

It has these top-level messages:
	Dataframe
	CanData
	CanMsg
	CanSchema
*/
package can

import proto "github.com/golang/protobuf/proto"
import fmt "fmt"
import math "math"

// Reference imports to suppress errors if they are not otherwise used.
var _ = proto.Marshal
var _ = fmt.Errorf
var _ = math.Inf

// This is a compile-time assertion to ensure that this generated file
// is compatible with the proto package it is being compiled against.
// A compilation error at this line likely means your copy of the
// proto package needs to be updated.
const _ = proto.ProtoPackageIsVersion2 // please upgrade the proto package

type Dataframe_Type int32

const (
	Dataframe_UINT64 Dataframe_Type = 0
)

var Dataframe_Type_name = map[int32]string{
	0: "UINT64",
}
var Dataframe_Type_value = map[string]int32{
	"UINT64": 0,
}

func (x Dataframe_Type) String() string {
	return proto.EnumName(Dataframe_Type_name, int32(x))
}
func (Dataframe_Type) EnumDescriptor() ([]byte, []int) { return fileDescriptor0, []int{0, 0} }

type CanMsg_Source int32

const (
	CanMsg_PLUTUS           CanMsg_Source = 0
	CanMsg_CHAOS            CanMsg_Source = 1
	CanMsg_TELEMETRY        CanMsg_Source = 2
	CanMsg_LIGHTS           CanMsg_Source = 3
	CanMsg_MOTOR_CONTROLLER CanMsg_Source = 4
	CanMsg_THEMIS           CanMsg_Source = 5
	CanMsg_RASPBERRY_PI     CanMsg_Source = 6
	CanMsg_MPPT_FRONT       CanMsg_Source = 7
	CanMsg_MPPT_REAR        CanMsg_Source = 8
)

var CanMsg_Source_name = map[int32]string{
	0: "PLUTUS",
	1: "CHAOS",
	2: "TELEMETRY",
	3: "LIGHTS",
	4: "MOTOR_CONTROLLER",
	5: "THEMIS",
	6: "RASPBERRY_PI",
	7: "MPPT_FRONT",
	8: "MPPT_REAR",
}
var CanMsg_Source_value = map[string]int32{
	"PLUTUS":           0,
	"CHAOS":            1,
	"TELEMETRY":        2,
	"LIGHTS":           3,
	"MOTOR_CONTROLLER": 4,
	"THEMIS":           5,
	"RASPBERRY_PI":     6,
	"MPPT_FRONT":       7,
	"MPPT_REAR":        8,
}

func (x CanMsg_Source) String() string {
	return proto.EnumName(CanMsg_Source_name, int32(x))
}
func (CanMsg_Source) EnumDescriptor() ([]byte, []int) { return fileDescriptor0, []int{2, 0} }

// NEXT TAG = 4
type Dataframe struct {
	Type  Dataframe_Type `protobuf:"varint,1,opt,name=type,enum=Dataframe_Type" json:"type,omitempty"`
	Start uint32         `protobuf:"varint,2,opt,name=start" json:"start,omitempty"`
	End   uint32         `protobuf:"varint,3,opt,name=end" json:"end,omitempty"`
}

func (m *Dataframe) Reset()                    { *m = Dataframe{} }
func (m *Dataframe) String() string            { return proto.CompactTextString(m) }
func (*Dataframe) ProtoMessage()               {}
func (*Dataframe) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{0} }

func (m *Dataframe) GetType() Dataframe_Type {
	if m != nil {
		return m.Type
	}
	return Dataframe_UINT64
}

func (m *Dataframe) GetStart() uint32 {
	if m != nil {
		return m.Start
	}
	return 0
}

func (m *Dataframe) GetEnd() uint32 {
	if m != nil {
		return m.End
	}
	return 0
}

// NEXT TAG = 3
type CanData struct {
	Data  uint64       `protobuf:"varint,1,opt,name=data" json:"data,omitempty"`
	Frame []*Dataframe `protobuf:"bytes,2,rep,name=frame" json:"frame,omitempty"`
}

func (m *CanData) Reset()                    { *m = CanData{} }
func (m *CanData) String() string            { return proto.CompactTextString(m) }
func (*CanData) ProtoMessage()               {}
func (*CanData) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{1} }

func (m *CanData) GetData() uint64 {
	if m != nil {
		return m.Data
	}
	return 0
}

func (m *CanData) GetFrame() []*Dataframe {
	if m != nil {
		return m.Frame
	}
	return nil
}

// NEXT TAG = 7
type CanMsg struct {
	Id          uint32        `protobuf:"varint,1,opt,name=id" json:"id,omitempty"`
	Source      CanMsg_Source `protobuf:"varint,2,opt,name=source,enum=CanMsg_Source" json:"source,omitempty"`
	IsAck       bool          `protobuf:"varint,3,opt,name=is_ack,json=isAck" json:"is_ack,omitempty"`
	GlobalMsgId uint32        `protobuf:"varint,4,opt,name=global_msg_id,json=globalMsgId" json:"global_msg_id,omitempty"`
	MsgName     string        `protobuf:"bytes,5,opt,name=msg_name,json=msgName" json:"msg_name,omitempty"`
	CanData     *CanData      `protobuf:"bytes,6,opt,name=can_data,json=canData" json:"can_data,omitempty"`
}

func (m *CanMsg) Reset()                    { *m = CanMsg{} }
func (m *CanMsg) String() string            { return proto.CompactTextString(m) }
func (*CanMsg) ProtoMessage()               {}
func (*CanMsg) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{2} }

func (m *CanMsg) GetId() uint32 {
	if m != nil {
		return m.Id
	}
	return 0
}

func (m *CanMsg) GetSource() CanMsg_Source {
	if m != nil {
		return m.Source
	}
	return CanMsg_PLUTUS
}

func (m *CanMsg) GetIsAck() bool {
	if m != nil {
		return m.IsAck
	}
	return false
}

func (m *CanMsg) GetGlobalMsgId() uint32 {
	if m != nil {
		return m.GlobalMsgId
	}
	return 0
}

func (m *CanMsg) GetMsgName() string {
	if m != nil {
		return m.MsgName
	}
	return ""
}

func (m *CanMsg) GetCanData() *CanData {
	if m != nil {
		return m.CanData
	}
	return nil
}

// NEXT TAG = 2
type CanSchema struct {
	Msg []*CanMsg `protobuf:"bytes,1,rep,name=msg" json:"msg,omitempty"`
}

func (m *CanSchema) Reset()                    { *m = CanSchema{} }
func (m *CanSchema) String() string            { return proto.CompactTextString(m) }
func (*CanSchema) ProtoMessage()               {}
func (*CanSchema) Descriptor() ([]byte, []int) { return fileDescriptor0, []int{3} }

func (m *CanSchema) GetMsg() []*CanMsg {
	if m != nil {
		return m.Msg
	}
	return nil
}

func init() {
	proto.RegisterType((*Dataframe)(nil), "Dataframe")
	proto.RegisterType((*CanData)(nil), "CanData")
	proto.RegisterType((*CanMsg)(nil), "CanMsg")
	proto.RegisterType((*CanSchema)(nil), "CanSchema")
	proto.RegisterEnum("Dataframe_Type", Dataframe_Type_name, Dataframe_Type_value)
	proto.RegisterEnum("CanMsg_Source", CanMsg_Source_name, CanMsg_Source_value)
}

func init() { proto.RegisterFile("can.proto", fileDescriptor0) }

var fileDescriptor0 = []byte{
	// 424 bytes of a gzipped FileDescriptorProto
	0x1f, 0x8b, 0x08, 0x00, 0x00, 0x09, 0x6e, 0x88, 0x02, 0xff, 0x44, 0x52, 0xcb, 0x8e, 0x9b, 0x40,
	0x10, 0x5c, 0x30, 0xcf, 0x76, 0x4c, 0x46, 0xa3, 0x8d, 0xc4, 0xde, 0x10, 0x91, 0x56, 0x9c, 0x38,
	0x38, 0x51, 0xae, 0x91, 0x43, 0x48, 0x8c, 0x04, 0x06, 0x35, 0xe3, 0xc3, 0x9e, 0xd0, 0x2c, 0x10,
	0x82, 0xd6, 0x60, 0xcb, 0x90, 0xc3, 0x7e, 0x44, 0xbe, 0x2c, 0x3f, 0x15, 0xcd, 0x60, 0x25, 0xb7,
	0x9e, 0xaa, 0xee, 0xea, 0xea, 0xd2, 0x80, 0x5d, 0xf3, 0x31, 0xbc, 0x5c, 0xcf, 0xf3, 0xd9, 0x3f,
	0x81, 0xfd, 0x95, 0xcf, 0xfc, 0xc7, 0x95, 0x0f, 0x2d, 0x7d, 0x0f, 0xda, 0xfc, 0x7a, 0x69, 0x5d,
	0xc5, 0x53, 0x02, 0x67, 0xfb, 0x36, 0xfc, 0xc7, 0x84, 0xec, 0xf5, 0xd2, 0xa2, 0x24, 0xe9, 0x3d,
	0xe8, 0xd3, 0xcc, 0xaf, 0xb3, 0xab, 0x7a, 0x4a, 0xb0, 0xc1, 0xe5, 0x41, 0x09, 0xac, 0xda, 0xb1,
	0x71, 0x57, 0x12, 0x13, 0xa5, 0x4f, 0x41, 0x13, 0x53, 0x14, 0xc0, 0x38, 0x26, 0x07, 0xf6, 0xe9,
	0x23, 0xb9, 0xf3, 0x3f, 0x83, 0x19, 0xf1, 0x51, 0xc8, 0x52, 0x0a, 0x5a, 0xc3, 0x67, 0x2e, 0x77,
	0x69, 0x28, 0x6b, 0xea, 0x81, 0x2e, 0xd7, 0xb9, 0xaa, 0xb7, 0x0a, 0xd6, 0x5b, 0xf8, 0x6f, 0x00,
	0x17, 0xc2, 0xff, 0xa3, 0x82, 0x11, 0xf1, 0x31, 0x9b, 0x3a, 0xea, 0x80, 0xda, 0x37, 0x72, 0x7c,
	0x83, 0x6a, 0xdf, 0xd0, 0x47, 0x30, 0xa6, 0xf3, 0xaf, 0x6b, 0xdd, 0x4a, 0x63, 0xce, 0xd6, 0x09,
	0x97, 0xc6, 0xb0, 0x94, 0x28, 0xde, 0x58, 0xfa, 0x0e, 0x8c, 0x7e, 0xaa, 0x78, 0xfd, 0x22, 0xcd,
	0x5a, 0xa8, 0xf7, 0xd3, 0xae, 0x7e, 0xa1, 0x3e, 0x6c, 0xba, 0xd3, 0xf9, 0x99, 0x9f, 0xaa, 0x61,
	0xea, 0xaa, 0xbe, 0x71, 0x35, 0xa9, 0xbc, 0x5e, 0xc0, 0x6c, 0xea, 0x92, 0x86, 0x3e, 0x80, 0x25,
	0xc8, 0x51, 0x58, 0xd4, 0x3d, 0x25, 0xb0, 0xd1, 0x1c, 0xa6, 0xee, 0xb0, 0x44, 0x67, 0xd5, 0x7c,
	0xac, 0xe4, 0x49, 0x86, 0xa7, 0x04, 0xeb, 0xad, 0x15, 0xde, 0x4e, 0x45, 0xb3, 0x5e, 0x0a, 0xff,
	0xb7, 0x02, 0xc6, 0xe2, 0x46, 0xa4, 0x52, 0xa4, 0x47, 0x76, 0x2c, 0xc9, 0x1d, 0xb5, 0x41, 0x8f,
	0xf6, 0xbb, 0xbc, 0x24, 0x0a, 0xdd, 0x80, 0xcd, 0xe2, 0x34, 0xce, 0x62, 0x86, 0x4f, 0x44, 0x15,
	0x5d, 0x69, 0xf2, 0x7d, 0xcf, 0x4a, 0xb2, 0xa2, 0xf7, 0x40, 0xb2, 0x9c, 0xe5, 0x58, 0x45, 0xf9,
	0x81, 0x61, 0x9e, 0xa6, 0x31, 0x12, 0x4d, 0x74, 0xb0, 0x7d, 0x9c, 0x25, 0x25, 0xd1, 0x29, 0x81,
	0x37, 0xb8, 0x2b, 0x8b, 0x2f, 0x31, 0xe2, 0x53, 0x55, 0x24, 0xc4, 0xa0, 0x0e, 0x40, 0x56, 0x14,
	0xac, 0xfa, 0x86, 0xf9, 0x81, 0x11, 0x53, 0xc8, 0xcb, 0x37, 0xc6, 0x3b, 0x24, 0x96, 0xff, 0x08,
	0x76, 0xc4, 0xc7, 0xb2, 0xfe, 0xd9, 0x0e, 0x9c, 0x3e, 0xc0, 0x6a, 0x98, 0x3a, 0x57, 0x91, 0xd1,
	0x9b, 0xb7, 0xf0, 0x50, 0x60, 0xcf, 0x86, 0xfc, 0x2b, 0x1f, 0xfe, 0x06, 0x00, 0x00, 0xff, 0xff,
	0x24, 0xc4, 0x19, 0x1b, 0x38, 0x02, 0x00, 0x00,
}
